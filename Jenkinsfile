pipeline {
    agent any

    parameters{
        choice(name: 'Vaihtoehdot', choices: ['Yksi', 'Kaksi', 'Kolme'], description: 'Tämä on vaihtoehtojen testi')
        string(name: 'Nimi', defaultValue: 'Vakionimi', description: 'Aseta tähän nimi')
        /*stashedFile 'testi.txt'
        stashedFile 'thumbnail.png'*/¨
        file(name: 'myTestFile', description: 'Enter a file')
        booleanParam(name: 'runDeployment', defaultValue: false, description: 'Toggle this to execute deployment stage')
        booleanParam(name: 'runTesting', defaultValue: false, description: 'Toggle this to execute testing stage')
        //file(name: 'testi.txt', description: 'Testausta')
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
        stage('Initial') {
            steps {
                script {
                    echo SECRET_INPUT
                    sh "chmod +x -R ${env.WORKSPACE}"
                    sh './test.sh'

                    //sh 'python3 test_my_application.py'
                    /*unstash 'testi.txt'
                    unstash 'thumbnail.png'*/

                    def file = file(params.myTestFile)

                    if (file && file.name.find(/\.png|jpg)$/)) {
                        echo 'This works'
                    }
                }
                
            }
        }

        stage('Deployment') {
            steps {
                script {
                    
                    if (params.runDeployment == true) {
                        
                        sh 'python3 test_my_application.py ' + "$workspace/thumbnail.png"
                    }

                    else {
                        sh 'echo Tämä stage on ohitettu'
                    }
                    

            

                
                }

                
                
                //input('Tämä on testi-inputti')
            }
        }

        stage('Testing') {
            steps {
                script{

                    catchError {

                        if (params.runTesting == true) {

                            sh "cat $workspace/t.txt"
                            echo 'Tämä vaihe suoritettiin'
                        }

                        else {
                            echo 'Tätä vaihetta ei suoriteta'
                        }
                    }
                    

                    
                }
                
            }
            
        }
    }
    
    post {
        
        always{
            echo 'Tämä on päättynyt'
            //sh "rm -rf $workspace/testi.txt"
        }
        
    }
}