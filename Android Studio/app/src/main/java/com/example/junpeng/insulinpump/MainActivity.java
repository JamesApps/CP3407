package com.example.junpeng.insulinpump;

import android.app.FragmentManager;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.design.widget.BottomNavigationView;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentTransaction;
import android.support.v7.app.AppCompatActivity;
import android.view.MenuItem;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    private TextView mTextMessage;
    
    private BottomNavigationView.OnNavigationItemSelectedListener mOnNavigationItemSelectedListener
            = new BottomNavigationView.OnNavigationItemSelectedListener() {

        @Override
        public boolean onNavigationItemSelected(@NonNull MenuItem item) {
            Fragment selectedFragment = null;
            switch (item.getItemId()) {
                case R.id.navigation_home:
                    selectedFragment = HomeFragment.newInstance();
                    return true;
                case R.id.navigation_history:
                    selectedFragment = HistoryFragment.newInstance();
                    //mTextMessage.setText(R.string.title_history);
                    return true;
                case R.id.navigation_driprate:
                    selectedFragment = DripFragment.newInstance();
                    //mTextMessage.setText(R.string.title_driprate);
                    return true;
                case R.id.navigation_settings:
                    selectedFragment = SettingsFragment.newInstance();
                    //mTextMessage.setText(R.string.title_settings);
                    return true;
                case R.id.navigation_insulin:
                    selectedFragment = InsulinFragment.newInstance();
                    //mTextMessage.setText(R.string.title_insulin);
                    return true;
            }
            FragmentTransaction transaction = getSupportFragmentManager().beginTransaction();
            transaction.replace(R.id.content, selectedFragment);
            transaction.commit();
            return true;
            //return false;
        }

    };

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mTextMessage = (TextView) findViewById(R.id.message);
        BottomNavigationView navigation = (BottomNavigationView) findViewById(R.id.navigation);
        navigation.setOnNavigationItemSelectedListener(mOnNavigationItemSelectedListener);
    }

}
