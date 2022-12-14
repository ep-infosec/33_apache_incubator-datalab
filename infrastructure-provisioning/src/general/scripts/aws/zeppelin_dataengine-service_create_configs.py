#!/usr/bin/python3

# *****************************************************************************
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
# ******************************************************************************

import argparse
import subprocess
from datalab.actions_lib import jars, yarn, install_emr_spark, spark_defaults, installing_python, configure_zeppelin_emr_interpreter
from datalab.common_lib import *
from datalab.fab import configuring_notebook, update_zeppelin_interpreters
from datalab.notebook_lib import *
from fabric import *

parser = argparse.ArgumentParser()
parser.add_argument('--bucket', type=str, default='')
parser.add_argument('--cluster_name', type=str, default='')
parser.add_argument('--dry_run', type=str, default='false')
parser.add_argument('--emr_version', type=str, default='')
parser.add_argument('--spark_version', type=str, default='')
parser.add_argument('--scala_version', type=str, default='')
parser.add_argument('--hadoop_version', type=str, default='')
parser.add_argument('--matplotlib_version', type=str, default='')
parser.add_argument('--region', type=str, default='')
parser.add_argument('--excluded_lines', type=str, default='')
parser.add_argument('--project_name', type=str, default='')
parser.add_argument('--os_user', type=str, default='')
parser.add_argument('--edge_hostname', type=str, default='')
parser.add_argument('--proxy_port', type=str, default='')
parser.add_argument('--livy_version', type=str, default='')
parser.add_argument('--multiple_clusters', type=str, default='')
parser.add_argument('--numpy_version', type=str, default='')
parser.add_argument('--application', type=str, default='')
parser.add_argument('--r_enabled', type=str, default='')
args = parser.parse_args()

emr_dir = '/opt/' + args.emr_version + '/jars/'
kernels_dir = '/home/' + args.os_user + '/.local/share/jupyter/kernels/'
spark_dir = '/opt/' + args.emr_version + '/' + args.cluster_name + '/spark/'
yarn_dir = '/opt/' + args.emr_version + '/' + args.cluster_name + '/conf/'
if args.region == 'us-east-1':
    endpoint_url = 'https://s3.amazonaws.com'
elif args.region == 'cn-north-1':
    endpoint_url = "https://s3.{}.amazonaws.com.cn".format(args.region)
else:
    endpoint_url = 'https://s3-{}.amazonaws.com'.format(args.region)


def install_remote_livy(args):
    subprocess.run('sudo chown ' + args.os_user + ':' + args.os_user + ' -R /opt/zeppelin/', shell=True, check=True)
    subprocess.run('sudo service zeppelin-notebook stop', shell=True, check=True)
    subprocess.run('sudo -i wget http://archive.cloudera.com/beta/livy/livy-server-' + args.livy_version + '.zip -O /opt/'
          + args.emr_version + '/' + args.cluster_name + '/livy-server-' + args.livy_version + '.zip', shell=True, check=True)
    subprocess.run('sudo unzip /opt/'
          + args.emr_version + '/' + args.cluster_name + '/livy-server-' + args.livy_version + '.zip -d /opt/'
          + args.emr_version + '/' + args.cluster_name + '/', shell=True, check=True)
    subprocess.run('sudo mv /opt/' + args.emr_version + '/' + args.cluster_name + '/livy-server-' + args.livy_version +
          '/ /opt/' + args.emr_version + '/' + args.cluster_name + '/livy/', shell=True, check=True)
    livy_path = '/opt/' + args.emr_version + '/' + args.cluster_name + '/livy/'
    subprocess.run('sudo mkdir -p ' + livy_path + '/logs', shell=True, check=True)
    subprocess.run('sudo mkdir -p /var/run/livy', shell=True, check=True)
    subprocess.run('sudo chown ' + args.os_user + ':' + args.os_user + ' -R /var/run/livy', shell=True, check=True)
    subprocess.run('sudo chown ' + args.os_user + ':' + args.os_user + ' -R ' + livy_path, shell=True, check=True)


if __name__ == "__main__":
    if args.dry_run == 'true':
        parser.print_help()
    else:
        result = prepare(emr_dir, yarn_dir)
        if result == False :
            jars(args, emr_dir)
        yarn(args, yarn_dir)
        install_emr_spark(args)
        spark_defaults(args)
        configuring_notebook(args.emr_version)
        if args.multiple_clusters == 'true':
            install_remote_livy(args)
        installing_python(args.region, args.bucket, args.project_name, args.cluster_name, args.application,
                          args.numpy_version, args.matplotlib_version)
        configure_zeppelin_emr_interpreter(args.emr_version, args.cluster_name, args.region, spark_dir, args.os_user,
                                           yarn_dir, args.bucket, args.project_name, endpoint_url, args.multiple_clusters)
        update_zeppelin_interpreters(args.multiple_clusters, args.r_enabled)
