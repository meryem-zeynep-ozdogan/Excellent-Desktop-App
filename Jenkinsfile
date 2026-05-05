pipeline {
    agent any
    
    environment {
        RUSTUP_HOME = "C:\\Users\\merzey\\.rustup"
        CARGO_HOME  = "C:\\Users\\merzey\\.cargo"
        // İŞTE GERÇEK YOLUN BU:
        PYO3_PYTHON = "C:\\Users\\merzey\\AppData\\Local\\Python\\bin\\python.exe"
    }
    
    stages {
        stage('Checkout') {
            steps { 
                git branch:'main', url:'https://github.com/meryem-zeynep-ozdogan/Excellent-Desktop-App.git' 
            }
        }
        
        stage('Rust QR Performance Check') {
            steps {
                echo 'Running Rust QR decoding algorithms...'
                dir('rust_qr') {
                    bat '"C:\\Users\\merzey\\.cargo\\bin\\cargo.exe" test' 
                }
            }
        }
        
        stage('Setup Python Environment') {
            steps {
                // Burayı da senin gerçek yolunla güncelledim
                bat '"C:\\Users\\merzey\\AppData\\Local\\Python\\bin\\python.exe" -m venv venv'
                bat 'venv\\Scripts\\python.exe -m pip install pytest'
            }
        }
        
        stage('Database Stress Test') {
            steps {
                echo 'Executing Database Integrity and Stress Tests...'
                bat 'venv\\Scripts\\python.exe tests/db_stress_test.py'
            }
        }

        stage('UI Asset & Logic Verification') {
            steps {
                echo 'Checking application assets and Input Validation...'
                bat 'venv\\Scripts\\pytest tests/test_ui_logic.py'
            }
        }
    }
    post {
        failure { echo 'PIPELINE FAILED! Missing assets or validation bug detected.' }
        success { echo 'ALL CLEAR! Ready for deployment.' }
    }
}