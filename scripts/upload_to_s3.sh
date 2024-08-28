# scripts/upload_to_s3.sh
aws s3 cp ../data/iris_train.csv s3://iris-train-data/iris_train.csv
aws s3 cp ../data/iris_test.csv s3://iris-test-data/iris_test.csv
