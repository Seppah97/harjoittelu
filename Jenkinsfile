pipeline {
    agent any

    parameters{
        choice(name: 'Vaihtoehdot', choices: ['Yksi', 'Kaksi', 'Kolme'], description: 'Tämä on vaihtoehtojen testi')
        string(name: 'Nimi', defaultValue: 'Vakionimi', description: 'Aseta tähän nimi')
        stashedFile 'testi.txt'
    }

    triggers {
        pollSCM('* * * * *')
    }

    environment {
        DB_ENGINE = 'sqlite'
        SECRET_INPUT = credentials('testi_secret')
    }

    options {
        buildDiscarder(logRotator(numToKeepStr: '10', artifactNumToKeepStr: '5'))
    }

    stages {
        stage('Test') {
            steps {
                echo SECRET_INPUT
                sh "chmod +x -R ${env.WORKSPACE}"
                sh './test.sh'

                sh 'python3 test_my_application.py'
            }
        }

        stage('Deployment') {
            steps {
                script {
                    unstash 'testi.txt'
                    cat "$workspace/testi.txt"
                    /*new hudson.FilePath(new File("$workspace/uusi.txt")).copyFrom(new hudson.FilePath("workspace/testipipeline/uusi.txt"))
                    archiveArtifacts artifacts: 'uusi.txt'*/
                    archiveArtifacts artifacts: 'testi.txt'



                
                }
                
                //input('Tämä on testi-inputti')
            }
        }
    }
    
    post {
        
        always{
            echo 'Tämä on päättynyt'
        }
        
    }
}