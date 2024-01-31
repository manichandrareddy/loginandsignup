package com.example.loginandsignup;

import android.content.Intent;
import android.os.Bundle;
import android.text.TextUtils;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ProgressBar;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FirebaseAuth;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

public class RegisterActivity extends AppCompatActivity {

    EditText fullName,email,password,phone;
    Button registerButton;
    TextView loginBtn;
    ProgressBar progressBar;
    FirebaseAuth firebaseAuth;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);
        fullName = findViewById(R.id.fullName);
        email = findViewById(R.id.email);
        password = findViewById(R.id.password);
        phone = findViewById(R.id.phone);
        registerButton =findViewById(R.id.registerButton);
        loginBtn = findViewById(R.id.createText);

        firebaseAuth = FirebaseAuth.getInstance();
        progressBar = findViewById(R.id.progressBar);

        if(firebaseAuth.getCurrentUser() != null){
            startActivity(new Intent(getApplicationContext(),MainActivity.class));
            finish();
        }

        registerButton.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v){
                    String memail=email.getText().toString().trim();
                String mpassword=password.getText().toString().trim();

                if(TextUtils.isEmpty(memail)){
                    email.setError("Email is required.");
                    return;
                }
                if(TextUtils.isEmpty(mpassword)){
                    password.setError("password is required.");
                    return;
                }
                if(password.length()<6){
                    password.setError("Password must be>=6 Characters");
                    return;
                }
                if(phone.length()<10){
                    phone.setError("Invalid number");
                    return;
                }

                progressBar.setVisibility(View.VISIBLE);
                firebaseAuth.createUserWithEmailAndPassword(memail,mpassword).addOnCompleteListener(new OnCompleteListener<AuthResult>() {
                    @Override
                    public void onComplete(@NonNull Task<AuthResult> task) {
                       if(task.isSuccessful()){
                           Toast.makeText(RegisterActivity.this,"User Created",Toast.LENGTH_SHORT).show() ;
                            startActivity(new Intent(getApplicationContext(),Login.class));}
                       else
                       {
                           Toast.makeText(RegisterActivity.this,"Error !!.."+ task.getException().getMessage(),Toast.LENGTH_SHORT).show() ;
                       }
                    }
                });
            }



        });

        loginBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(getApplicationContext(),Login.class));
            }
        });






    }
}
