pipeline {
  agent any
  environment {
    IMAGE_NAME = 'salsabillaputriip/simple-app'
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

    stage('Unit Test') {
      steps {
        sh '''
          pip install -r requirements.txt
          pytest --maxfail=1 --disable-warnings -q
        '''
      }
    }

    stage('Build Docker Image') {
      when {
        expression { currentBuild.resultIsBetterOrEqualTo('SUCCESS') }
      }
      steps {
        script {
          docker.build("${IMAGE_NAME}:${env.BUILD_NUMBER}")
        }
      }
    }

    stage('Push Docker Image') {
      when {
        expression { currentBuild.resultIsBetterOrEqualTo('SUCCESS') }
      }
      steps {
        script {
          docker.withRegistry(REGISTRY, REGISTRY_CREDENTIALS) {
            def tag = "${IMAGE_NAME}:${env.BUILD_NUMBER}"
            docker.image(tag).push()
            docker.image(tag).push('latest')
          }
        }
      }
    }
  }
  post {
    always {
      echo 'Pipeline selesai dijalankan'
    }
  }
}
