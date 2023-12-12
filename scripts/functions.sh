#!/bin/bash

function api_call(){
  local url="${1:?api_call: url undefined}" ; shift
  local method="${1:-GET}" ; shift
  local data="{${BR:+ \"ref\":\"$BR\"}}"
  curl -s -X$method -H "Accept: application/vnd.github.v3+json" ${TOK:+ -H "authorization: Bearer $TOK"} -d "$data" "$url" $@
}

function api_get_trigrun(){
  local url=${1:?"api_call: url undefined"} ; shift
  local event="${1:-workflow_dispatch}" ; shift
  local concl="$1" ; shift
  local idx="${1:-0}" ; shift
  local status="${concl:+"&status=$concl"}"
  local cond='.path==".github/workflows/manual.yaml"'
  local fullurl="$url/actions/runs?branch=$BR&actor=$BOT&event=$event$status"
  api_call "$fullurl" "GET" | jq -r "
    [
      .workflow_runs[]
      | select($cond)
    ]
    | sort_by(.run_started_at) | reverse [$idx]
    | [.run_started_at,.conclusion]
    |@tsv
  "
}

function mm_msg(){
  local msg="${1:-Incoming Webhook test $(date '+%y%m%d-%H%M%S')}"
  shift
  local channel="$1"
  shift
  local url="${MM_OAREPO_WH:?Error, MM_OAREPO_WH undefined}"
  local opts='-H "Content-Type: application/json"'
  local data="{\"text\":\"$msg\"${channel:+, \"channel\":\"$channel\"}}"
  curl -s -X POST -H "Content-Type: application/json" -d "$data" "$url"
}
