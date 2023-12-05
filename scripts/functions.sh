#!/bin/bash

function api_call(){
  local url="${1:?api_call: url undefined}" ; shift
  local method="${1:-GET}" ; shift
  local data="{${BR:+ \"ref\":\"$BR\"}}"
  curl -s -X$method -H "Accept: application/vnd.github.v3+json" ${TOK:+ -H "authorization: Bearer $TOK"} -d "$data" "$url" $@
}

function api_get_trigrun(){
#  local url=${1:?api_call: url undefined} ; shift
#  local event=${1:-workflow_dispatch} ; shift
#  echo "api_get_trigrun($url, $event, BR=$BR, BOT=$BOT)"
  local url=$1
  echo "api_get_trigrun($url, BR=$BR, BOT=$BOT)"
#  api_call "$url/actions/runs" "GET" | jq -r '
#    [
#      .workflow_runs[]
#      | select(.head_branch=="'$BR'" and .path==".github/workflows/manual.yaml" and .actor.login=="'$BOT'" and .event=="'$event'")
#    ]
#    | sort_by(.run_started_at) | reverse [0]
#    | [.run_started_at,.conclusion]
#    |@tsv
#  '
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
