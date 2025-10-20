pipeline {
  agent any

  environment {
    // Ganti 'awanmh/simple-app' dengan nama image dan repo kamu di Docker Hub
    IMAGE_NAME = 'salsabillaputriip/simple-app'
    // Registry default Docker Hub
    REGISTRY = 'https://index.docker.io/v1/'
    // Ganti 'dockerhub-credentials' dengan ID credential Docker Hub kamu di Jenkins
    REGISTRY_CREDENTIALS = 'dockerhub-credentials'
  }

  stages {

    stage('Checkout') {
      steps {
        echo 'Checkout source code...'
        checkout scm
      }
    }

    stage('Build') {
      steps {
        sh 'echo "Mulai build aplikasi (Linux/Mac)"'
      }
    }
    stage('Push Docker Image') {
      steps {
        script {
          echo "Push Docker image ke Docker Hub..."
    
          docker.withRegistry(env.REGISTRY, env.REGISTRY_CREDENTIALS) {
            def tag = "${env.IMAGE_NAME}:${env.BUILD_NUMBER}"
    
            // Push dengan tag build number
            docker.image(tag).push()
    
            // Tambahkan tag 'latest' dan push juga
            docker.image(tag).tag('latest')
            docker.image("${env.IMAGE_NAME}:latest").push()
          }
        }
      }
    }
  }

  post {
    always {
      echo 'Selesai build pipeline.'
    }
  }
}
