pipeline {
    agent {
        label 'kesariya'
    }
    stages {
        stage('Code Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/rakshithgr7/my-exciting-project'
            }
        }
        stage('CI') {
            steps {
                sh 'python3 $WORKSPACE/jenkins/TestCalculator.py'
            }
        }
        stage('CD') {
            environment {
                STACK_NAME = 'cont-del'
                S3_BUCKET = 'mybucket-nk2'
            }
            steps {
                withAWS(credentials: 'foraws', region: 'ap-south-1') {
                    sh 'sam deploy --stack-name $STACK_NAME -t template.yaml --s3-bucket $S3_BUCKET --capabilities CAPABILITY_IAM'
                }
            }
        }
    }
}
