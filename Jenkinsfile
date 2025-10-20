pipeline {
  agent any
  environment {
    IMAGE_NAME = 'Calcuiii/simple-app'
    REGISTRY = 'https://index.docker.io/v1/'
    REGISTRY_CREDENTIALS = 'dockerhub-credentials'
  }
  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    stage('Build') {
      steps {
        sh 'echo "Mulai build aplikasi"'
      }
    }
    stage('Build Docker Image') {
      steps {
        script {
          docker.build("${env.IMAGE_NAME}:${env.BUILD_NUMBER}")
        }
      }
    }
    stage('Push Docker Image') {
      steps {
        script {
          docker.withRegistry(env.REGISTRY, env.REGISTRY_CREDENTIALS) {
            def tag = "${env.IMAGE_NAME}:${env.BUILD_NUMBER}"
            docker.image(tag).push()
            docker.image(tag).tag('latest')
            docker.image("${env.IMAGE_NAME}:latest").push()
          }
        }
      }
    }
  }
  post {
    always {
      echo 'Selesai build'
    }
  }
}
