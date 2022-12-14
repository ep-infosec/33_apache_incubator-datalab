# *****************************************************************************
#
#  Licensed to the Apache Software Foundation (ASF) under one
#  or more contributor license agreements.  See the NOTICE file
#  distributed with this work for additional information
#  regarding copyright ownership.  The ASF licenses this file
#  to you under the Apache License, Version 2.0 (the
#  "License"); you may not use this file except in compliance
#  with the License.  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing,
#  software distributed under the License is distributed on an
#  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#  KIND, either express or implied.  See the License for the
#  specific language governing permissions and limitations
#  under the License.
#
# ******************************************************************************

variable "project_tag" {}

variable "endpoint_tag" {}

variable "user_tag" {}

variable "custom_tag" {}

variable "region" {}

variable "product" {}

variable "vpc_name" {}

variable "fw_ingress" {}

variable "fw_egress_public" {}

variable "fw_egress_private" {}

variable "network_tag" {}

variable "cidr_range" {}

variable "traefik_cidr" {}

variable "ps_roles" {
  type = list(string)
  default = [
    "roles/dataproc.worker"
  ]
}

variable "ps_policy" {
  type = list(string)
  default = [

  ]
}