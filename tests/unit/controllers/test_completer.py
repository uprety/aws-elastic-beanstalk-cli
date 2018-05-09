# Copyright 2015 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

import mock

from .basecontrollertest import BaseControllerTest

from ebcli.core import fileoperations
from ebcli.objects.solutionstack import SolutionStack
from ebcli.objects.tier import Tier


class TestCompleter(BaseControllerTest):
    solution = SolutionStack('64bit Amazon Linux 2014.03 '
                             'v1.0.6 running PHP 5.5')
    app_name = 'ebcli-test-app'
    tier = Tier.get_default()

    def setUp(self):
        self.module_name = 'create'
        super(TestCompleter, self).setUp()
        fileoperations.create_config_file(self.app_name, 'us-west-2',
                                          self.solution.name)

    def test_base_commands(self):
        """
        testing for base controllers
        """

        # run cmd
        self.run_command('completer', '--cmplt', ' ')

        output = set(self.mock_output.call_args[0])

        # Its best to hard code this
        # That way we can make sure this list matches exactly
        # What we would expect, nothing more.
        expected = {
            'logs',
            'terminate',
            'abort',
            'open',
            'use',
            'scale',
            'console',
            'create',
            'platform',
            'init',
            'setenv',
            'swap',
            'events',
            'status',
            'labs',
            'upgrade',
            'ssh',
            'config',
            'list',
            'printenv',
            'local',
            'health',
            'tags'
            }

        self.assertEqual(expected, output)
