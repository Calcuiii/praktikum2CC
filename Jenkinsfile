pipeline {
  agent any

  options {
    timestamps()
    ansiColor('xterm')
    buildDiscarder(logRotator(numToKeepStr: '20'))
    timeout(time: 30, unit: 'MINUTES')
  }

  environment {
    IMAGE_NAME            = 'salsabillaputriip/simple-app'
    REGISTRY              = 'https://index.docker.io/v1/'
    REGISTRY_CREDENTIALS  = 'dockerhub-credentials'
    DOCKER_CLI            = '/Applications/Docker.app/Contents/Resources/bin/docker'
    PATH                  = '/Applications/Docker.app/Contents/Resources/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin'
  }

  stages {

    stage('Checkout') {
      steps {
        checkout scm
        echo 'Code checked out successfully'
      }
    }

    stage('Build (Prepare)') {
      steps {
        sh '''
          echo "Mulai build aplikasi"
          python3 --version || python --version
          which pip3 || which pip || true
        '''
      }
    }

    stage('Unit Test') {
      steps {
        echo 'Running Unit Tests...'
        sh '''
          # Install dependencies
          python3 -m pip install --user -r requirements.txt

          # Jalankan pytest
          python3 -m pytest --maxfail=1 --disable-warnings -v test_app.py

          echo "All tests passed successfully!"
        '''
      }
      post {
        failure {
          echo 'Unit tests failed! Pipeline stopped.'
          error('Unit tests failed - Build will not proceed')
        }
        success {
          echo 'Unit tests passed! Proceeding to build Docker image.'
        }
      }
    }

    stage('Build Docker Image') {
      when { expression { currentBuild.result == null || currentBuild.result == 'SUCCESS' } }
      steps {
        script {
          echo "Building Docker image: ${IMAGE_NAME}:${env.BUILD_NUMBER}"
          docker.build("${IMAGE_NAME}:${env.BUILD_NUMBER}")
          echo 'Docker image built successfully'
        }
      }
    }

    stage('Push Docker Image') {
      when { expression { currentBuild.result == null || currentBuild.result == 'SUCCESS' } }
      steps {
        script {
          echo 'Pushing Docker image to Docker Hub...'
          docker.withRegistry("${REGISTRY}", "${REGISTRY_CREDENTIALS}") {
            // Push tag build number
            docker.image("${IMAGE_NAME}:${env.BUILD_NUMBER}").push()

            // Tag latest & push
            sh "docker tag ${IMAGE_NAME}:${env.BUILD_NUMBER} ${IMAGE_NAME}:latest"
            docker.image("${IMAGE_NAME}:latest").push()
          }
          echo "Successfully pushed ${IMAGE_NAME}:${env.BUILD_NUMBER} and ${IMAGE_NAME}:latest"
        }
      }
    }
  }

  post {
    always {
      echo 'Pipeline selesai dijalankan'
    }
    success {
      echo 'Pipeline berhasil! Image telah dipush ke Docker Hub.'
    }
    failure {
      echo 'Pipeline gagal! Periksa log untuk detail error.'
    }
  }
}
