package com.example.loginandsignup;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import com.google.firebase.auth.FirebaseAuth;

import androidx.appcompat.app.AppCompatActivity;

public class Combo extends AppCompatActivity implements View.OnClickListener {
    Button OrderDetailsbtn;
    Button Homebtn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_combo);
        OrderDetailsbtn = findViewById(R.id.orderDetails);
        Homebtn=findViewById(R.id.Home);
        OrderDetailsbtn.setOnClickListener(this);
        Homebtn.setOnClickListener(this);
    }

    public void logout(View view) {
        FirebaseAuth.getInstance().signOut();//logout
        startActivity(new Intent(getApplicationContext(), Login.class));
        finish();
    }

    public void onClick(View v) {
        switch (v.getId()) {
            case R.id.orderDetails:
                Intent intent = new Intent(this.getApplicationContext(), orderDetails.class);
                this.startActivity(intent);
                break;
            case R.id.Home:
                Intent intent1 = new Intent(this.getApplicationContext(),MainActivity.class);
                this.startActivity(intent1);
                break;
        }
    }
}