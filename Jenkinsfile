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
                failure {
                    mail to: 'tanner@real-time.com'
                    subject: "Failed Pipeline: ${currentBuild.fullDisplayName}",
                    body: "Something is wrong with ${env.BUILD_URL}"
                }
                success {
                    slackSend channel: '#gitlab',
                    color: 'good',
                    message: "The pipeline ${currentBuild.fullDisplayName} completed successfully."
                }
            }
        }
    }
}
