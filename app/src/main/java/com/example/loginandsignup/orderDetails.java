package com.example.loginandsignup;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import com.google.firebase.auth.FirebaseAuth;

import androidx.appcompat.app.AppCompatActivity;

public class orderDetails extends AppCompatActivity implements View.OnClickListener {
    Button Combobtn;
    Button Homebtn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_order_details);
        Combobtn = findViewById(R.id.Combo);
        Homebtn=findViewById(R.id.Home);
        Homebtn.setOnClickListener(this);
        Combobtn.setOnClickListener(this);
    }

    public void logout(View view) {
        FirebaseAuth.getInstance().signOut();//logout
        startActivity(new Intent(getApplicationContext(), Login.class));
        finish();
    }

    public void onClick(View v) {
        switch (v.getId()) {

            case R.id.Combo:
                Intent intent = new Intent(this.getApplicationContext(), Combo.class);
                this.startActivity(intent);
                break;
            case R.id.Home:
                Intent intent1 = new Intent(this.getApplicationContext(),MainActivity.class);
                this.startActivity(intent1);
                break;


        }
    }
}