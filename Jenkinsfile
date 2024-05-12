pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                script {
                    checkout([$class: 'GitSCM', branches:[[name: 'master']], userRemoteConfigs: [[url:'https://github.com/Yadu-krishnan-c/Devops-assignment.git', credentialsId:'Bits-Git']]])
                }
            }
        }

        stage('hello_world') {
            steps {
                echo 'Python run'
                sh 'dir'
                sh 'python3 hello_world.py'
            }
        }

        stage('Password_checker') {
            steps {
                echo 'Task bot Design'
                sh 'python3 design.py'
            }
        }
    }
}