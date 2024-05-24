import unittest
from unittest.mock import patch, MagicMock
from airflow.models import DagBag, TaskInstance
from datetime import datetime
import logging

class TestDataPipelineDAG(unittest.TestCase):

    def setUp(self):
        self.dagbag = DagBag()

    def test_dag_import(self):
        """Test if the DAG is correctly imported"""
        dag = self.dagbag.get_dag(dag_id='data_pipeline')
        self.assertIsNotNone(dag)
        self.assertEqual(len(dag.tasks), 2)

    def test_task_dependencies(self):
        """Test task dependencies of the DAG"""
        dag = self.dagbag.get_dag(dag_id='data_pipeline')
        collect_task = dag.get_task(task_id='collect_data')
        process_task = dag.get_task(task_id='process_data')

        self.assertEqual(collect_task.downstream_list, [process_task])
        self.assertEqual(process_task.upstream_list, [collect_task])

if __name__ == '__main__':
    unittest.main()
