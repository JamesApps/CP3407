package com.example.junpeng.insulinpump;

import android.app.FragmentManager;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.design.widget.BottomNavigationView;
import android.support.v7.app.AppCompatActivity;
import android.view.MenuItem;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    private TextView mTextMessage;


    private BottomNavigationView.OnNavigationItemSelectedListener mOnNavigationItemSelectedListener
            = new BottomNavigationView.OnNavigationItemSelectedListener() {

        @Override
        public boolean onNavigationItemSelected(@NonNull MenuItem item) {
            //FragmentManager fm = getFragmentManager();
            switch (item.getItemId()) {
                case R.id.navigation_home:
                    mTextMessage.setText(R.string.title_home);
                    //fm.beginTransaction().replace(R.id.container, new HomeFragment()).commit();
                    return true;
                case R.id.navigation_history:
                    mTextMessage.setText(R.string.title_history);
                    //fm.beginTransaction().replace(R.id.container, new HistoryFragment()).commit();
                    return true;
                case R.id.navigation_driprate:
                    mTextMessage.setText(R.string.title_driprate);
                    //fm.beginTransaction().replace(R.id.container, new DripFragment()).commit();
                    return true;
                case R.id.navigation_settings:
                    mTextMessage.setText(R.string.title_settings);
                    //fm.beginTransaction().replace(R.id.container, new SettingsFragment()).commit();
                    return true;
                case R.id.navigation_insulin:
                    mTextMessage.setText(R.string.title_insulin);
                    //fm.beginTransaction().replace(R.id.container, new InsulinFragment()).commit();
                    return true;
            }
            return false;
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
