pipeline {
  agent any
  stages {
    stage('Checkout repository') {
      steps {
        sh 'echo CheckoutGit'
        git 'https://github.com/yehiamc/worldOfGames.git'
      }
    }
    stage('Build Docker image') {
      steps{
      sh 'echo BuildDockerImage'
      sh 'docker-compose build'
      }
    }
    stage('Run Docker') {
      steps{
      sh 'echo running Docker'
      sh 'docker-compose up -d'
      }
    }

    stage('e2e test') {
      steps{
      sh 'echo e2e test'
      sh 'python tests/e2e.py'
      }
    }

  
    stage('Finalize'){
      steps{
      sh 'echo Stop the container'
      sh 'docker-compose down'
      }
    }  
  }
}