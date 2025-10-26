pipeline {
  agent any
  environment {
    IMAGE_NAME = 'salsabillaputriip/simple-app'
    REGISTRY = 'https://index.docker.io/v1/'
    REGISTRY_CREDENTIALS = 'dockerhub-credentials'
    DOCKER_CLI = "/Applications/Docker.app/Contents/Resources/bin/docker"
    PATH = "/Applications/Docker.app/Contents/Resources/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
  }
  stages {
    stage('Checkout') {
      steps {
        checkout scm
        echo 'Code checked out successfully'
      }
    }
    
    stage('Build') {
      steps {
        sh 'echo "Mulai build aplikasi"'
        sh 'python3 --version || python --version'
        sh 'which pip3 || which pip'
      }
    }
    
    stage('Unit Test') {
      steps {
        script {
          echo 'Running Unit Tests...'
          sh '''
            # Install dependencies using pip3
            python3 -m pip install --user -r requirements.txt
            
            # Run pytest with verbose output
            python3 -m pytest --maxfail=1 --disable-warnings -v test_app.py
            
            echo "All tests passed successfully!"
          '''
        }
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
      when {
        expression { currentBuild.result == null || currentBuild.result == 'SUCCESS' }
      }
      steps {
        script {
          echo "Building Docker image: ${IMAGE_NAME}:${env.BUILD_NUMBER}"
          docker.build("${IMAGE_NAME}:${env.BUILD_NUMBER}")
          echo "Docker image built successfully"
        }
      }
    }
    
    stage('Push Docker Image') {
      when {
        expression { currentBuild.result == null || currentBuild.result == 'SUCCESS' }
      }
      steps {
        script {
          echo "Pushing Docker image to registry..."
          docker.withRegistry(REGISTRY, REGISTRY_CREDENTIALS) {
            def tag = "${IMAGE_NAME}:${env.BUILD_NUMBER}"
            docker.image(tag).push()
            docker.image(tag).push('latest')
            echo "Docker image pushed successfully: ${tag}"
          }
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
