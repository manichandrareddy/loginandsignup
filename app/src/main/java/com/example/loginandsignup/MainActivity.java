package com.example.loginandsignup;


import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import com.google.firebase.auth.FirebaseAuth;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity implements View.OnClickListener {

   Button OrderDetailsbtn;
   Button Combobtn;
   Button addbtn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        OrderDetailsbtn=findViewById(R.id.orderDetails);
        Combobtn=findViewById(R.id.Combo);
        addbtn=findViewById(R.id.add);
        OrderDetailsbtn.setOnClickListener(this);
        Combobtn.setOnClickListener(this);
        addbtn.setOnClickListener(this);
    }



    public void logout(View view) {
        FirebaseAuth.getInstance().signOut();//logout
        startActivity(new Intent(getApplicationContext(),Login.class));
        finish();
    }

    @Override
    public void onClick(View v) {
        switch(v.getId())
        {
            case R.id.orderDetails:
                Intent intent = new Intent(this.getApplicationContext(),orderDetails.class);
                this.startActivity(intent);
                break;
            case R.id.Combo:
                Intent intent1= new Intent(this.getApplicationContext(),Combo.class);
                this.startActivity(intent1);
                break;
            case R.id.add:
                Intent intent2 = new Intent(this.getApplicationContext(),add.class);
                this.startActivity(intent2);
                break;


        }
    }
}
