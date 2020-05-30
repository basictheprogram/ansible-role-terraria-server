pipeline {
    agent {
        docker {
            imaage:'geerlingguy/docker-ubuntu2004-ansible:latest'
        }
    }
    stages {
        stage('Test') {
            docker {}
            steps {
                sh 'ansible --version'
            }
            post {
                always {
                    junit 'test-reports/results.xml' 
                }
            }
        }
    }
}
