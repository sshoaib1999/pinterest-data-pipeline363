from airflow import DAG
from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator 
from datetime import datetime, timedelta

notebook_task = {
    'notebook_path': '<DATABRICKS_NOTEBOOK_PATH>' 
}

default_args = {
    'owner': '0e09f2683831',
    'depends_on_past': False,    
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    
    dag_id='0e09f2683831_dag', 
    start_date=datetime(2023, 3, 13),  
    schedule_interval='@daily',
    default_args=default_args
) as dag:
    submit_run = DatabricksSubmitRunOperator(
        task_id='submit_run',
        existing_cluster_id=cluster_id, 
        notebook_task=notebook_task
    )
