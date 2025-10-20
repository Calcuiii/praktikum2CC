pipeline {
  agent any

  environment {
    IMAGE_NAME = 'salsabillaputriip/simple-app'              
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
        sh 'echo "Mulai build aplikasi (Linux)"'
      }
    }

    stage('Build Docker Image') {
      steps {
        withCredentials([usernamePassword(credentialsId: env.REGISTRY_CREDENTIALS, usernameVariable: 'USER', passwordVariable: 'PASS')]) {
          sh """
            echo "Login Docker sebelum build..."
            echo "$PASS" | docker login -u "$USER" --password-stdin
            docker build -t ${env.IMAGE_NAME}:${env.BUILD_NUMBER} .
            docker logout
          """
        }
      }
    }

    stage('Push Docker Image') {
      steps {
        withCredentials([usernamePassword(credentialsId: env.REGISTRY_CREDENTIALS, usernameVariable: 'USER', passwordVariable: 'PASS')]) {
          sh """
            echo "Login Docker untuk push..."
            echo "$PASS" | docker login -u "$USER" --password-stdin
            docker push ${env.IMAGE_NAME}:${env.BUILD_NUMBER}
            docker tag ${env.IMAGE_NAME}:${env.BUILD_NUMBER} ${env.IMAGE_NAME}:latest
            docker push ${env.IMAGE_NAME}:latest
            docker logout
          """
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
