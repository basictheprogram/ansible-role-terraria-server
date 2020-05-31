#!groovy

pipeline {
    agent none
    stages {
        stage('Docker Image Install') {
            agent {
                docker { 
                    image 'geerlingguy/docker-ubuntu2004-ansible:latest'
                }
            }
            steps {
                sh 'python3 -V'    
            }
        }
        stage('Check out the codebase') {
            agent any
            steps {
                checkout scm
            }
        }
        stage('Install test dependencies') {
            agent any
            steps {
                sh 'pip3 install molecule docker yamllint ansible-lint'
            }
        }
        stage('Run molecule tests') {
            agent any
            steps {
                sh 'ansible --version'
                sh 'molecule tests'
            }
            post {
                always {
                    echo 'One way or another, I have finished'
                    deleteDir()
                }
            }
        }
    }
}
