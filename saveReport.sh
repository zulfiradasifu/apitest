#!/bin/bash
cd /home/ubuntu/Desktop/API_tests/ && \
pytest -vvv . --html=reports/report.html --self-contained-html; \
/usr/local/bin/aws s3 sync /home/ubuntu/Desktop/API_tests/reports/ s3://ssw-apitest-reports