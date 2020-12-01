# Copyright 2020 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Abstraction for data ingestion logic."""

import abc


class NotApplicableError(ValueError):
    """This kind of ingester cannot be constructed from the given flags."""


class DataIngester(metaclass=abc.ABCMeta):
    """Link between a data source and a data provider.

    A data ingester starts a reload operation in the background and
    provides a data provider as a view.
    """

    @abc.abstractmethod
    def __init__(self, flags):
        """Creates a data ingester from flags.

        Args:
          flags: An argparse.Namespace containing TensorBoard CLI flags.

        Returns:
          The new data ingester.

        Raises:
          NotApplicableError: If this kind of data ingester is not
            applicable for an invocation with the given flags. This is
            not necessarily a fatal error; it indicates that the next
            ingester kind should be tried.
        """
        pass

    @property
    @abc.abstractmethod
    def data_provider(self):
        """Returns a `DataProvider`.

        It may be an error to dereference this before `start` is called.
        """
        pass

    @property
    @abc.abstractmethod
    def deprecated_multiplexer(self):
        """Returns a `PluginEventMultiplexer`, or `None` if not applicable.

        It may be an error to dereference this before `start` is called.
        """
        pass

    @abc.abstractmethod
    def start(self):
        """Starts ingesting data based on the ingester flag configuration.

        Must only be called once.
        """
        pass
