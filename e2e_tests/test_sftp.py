"""Test against SFTP docker image."""
from filetransferautomation.models import Host
from filetransferautomation.step_plugins.sftp import Download, Upload

"""
docker run --name sftp -v ${PWD}/e2e_data/sftp.json:/app/config/sftp.json:ro \
    -p 2222:22 -d emberstack/sftp
"""

USER = "bob"
HOST = "localhost"
PASS = "12345"


def test_sftp_upload():
    """SFTP upload test."""
    host = Host(
        username=USER,
        password=PASS,
        host=HOST,
        port=2222,
        directory="",
    )
    download = Upload(
        arguments='{"file_filter":"test.txt", "delete_files":true}',
        variables={
            "host": host,
            "workspace_directory": ".",
            "workspace_id": "test",
            "step_id": 1,
            "task_id": 1,
        },
    )
    download.process()


def test_sftp_download():
    """SFTP download test."""
    host = Host(
        username=USER,
        password=PASS,
        host=HOST,
        port=2222,
        directory="",
    )
    download = Download(
        arguments='{"file_filter":"test.txt", "delete_files":true}',
        variables={
            "host": host,
            "workspace_directory": ".",
            "workspace_id": "test",
            "step_id": 1,
            "task_id": 1,
        },
    )
    download.process()