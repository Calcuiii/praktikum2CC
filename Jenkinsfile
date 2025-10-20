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

    stage('Build Docker Image') {
      steps {
        script {
          echo "Building Docker image ${env.IMAGE_NAME}:${env.BUILD_NUMBER}..."
          docker.build("${env.IMAGE_NAME}:${env.BUILD_NUMBER}")
        }
      }
    }

    stage('Push Docker Image') {
        steps {
          script {
            echo "Push Docker image ke Docker Hub..."
      
            sh '''
              echo "Login ke Docker Hub..."
              docker login -u salsabillaputriip -p $DOCKER_HUB_PASS
      
              echo "Push image ke Docker Hub..."
              IMAGE_NAME=salsabillaputriip/simple-app
              TAG=${BUILD_NUMBER}
      
              # Push tag dengan nomor build
              docker push ${IMAGE_NAME}:${TAG}
      
              # Tag sebagai latest dan push juga
              docker tag ${IMAGE_NAME}:${TAG} ${IMAGE_NAME}:latest
              docker push ${IMAGE_NAME}:latest
            '''
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
