#!/bin/bash

function api_call(){
  local url="${1:?api_call: url undefined}" ; shift
  local method="${1:-GET}"
  local data="{${BR:+ \"ref\":\"$BR\"}}"
  curl -s -X$method -H "Accept: application/vnd.github.v3+json" ${TOK:+ -H "authorization: Bearer $TOK"} -d "$data" "$url" $@
}

function api_get_trigrun(){
  local url=${1:?"api_call: url undefined"} ; shift
  local event="${1:-workflow_dispatch}" ; shift
  local concl="$1" ; shift
  local idx="${1:-0}" ; shift
  local page=${1:-1}
  local concl_cond="${concl:+" and .conclusion==\"$concl\""}" ; shift
  local cond='.head_branch=="'$BR'" and .path==".github/workflows/manual.yaml" and .actor.login=="'$BOT'" and .event=="'$event'"'$concl_cond
  #echo ">$cond<"
  local r=$(api_call "$url/actions/runs?page=$page" "GET" | jq -r "
    [
      .workflow_runs[]
      | select($cond)
    ]
    | sort_by(.run_started_at) | reverse [$idx]
    | [.run_started_at,.conclusion]
    |@tsv
  ")
  #echo "$page: >$r<"
  if [[ "$r" == "\t" || $page -ne 1 ]]; then
    echo $r
  else
    api_get_trigrun "$url" "$event" "$concl" "$idx" 2
  fi
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
