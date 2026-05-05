pipeline {
    agent any
    triggers { pollSCM('H/5 * * * *') } 
    
    stages {
        stage('Checkout') {
            steps { 
                // Senin yeni repondan kodları çekiyoruz
                git branch:'main', url:'https://github.com/meryem-zeynep-ozdogan/Excellent-Desktop-App.git' 
            }
        }
        
        stage('Setup Python Environment') {
            steps {
                bat '''
                python -m venv venv
                call venv\\Scripts\\activate.bat
                pip install pytest
                '''
            }
        }
        
        stage('Rust QR Module Tests') {
            steps {
                // Rust klasörüne gidip testleri çalıştırıyoruz
                // EĞER RUST KODLARIN ANA DİZİNDEYSE SADECE 'cargo test' YAZABİLİRSİN
                dir('rust_qr') { 
                    bat 'cargo test'
                }
            }
        }
        
        stage('Python Financial & UI Tests') {
            steps {
                bat '''
                call venv\\Scripts\\activate.bat
                pytest --junitxml=python_test_raporu.xml
                '''
            }
            post { 
                always { 
                    junit 'python_test_raporu.xml' 
                } 
            }
        }
    }
    post {
        failure { echo 'Jenkins Pipeline: Build FAILED! Bozuk kod deploy edilemez.' }
        success { echo 'Jenkins Pipeline: All tests passed successfully!' }
    }
}