package com.example.junpeng.insulinpump;

import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.TextView;

public class HomeFragment extends Fragment {
    public static HomeFragment newInstance() {
        HomeFragment fragment = new HomeFragment();
        return fragment;
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        return inflater.inflate(R.layout.home_fragment, container, false);
    }
    @Override
    public void onViewCreated(View view, @Nullable Bundle savedInstanceState) {
        TextView textView = (TextView) getView().findViewById(R.id.textView2);
        textView.setText("Home");
        TextView textView1 = (TextView) getView().findViewById(R.id.textView6);
        textView1.setText("BG/Level");
        TextView textView2 = (TextView) getView().findViewById(R.id.textView5);
        textView2.setText("Pump:");
        TextView textView3 = (TextView) getView().findViewById(R.id.BGlevel);
        textView3.setText("\\t\\t\\tmmol/l"); //Blood Gluscose Level data reading goes here

        Button setButton = (Button) getView().findViewById(R.id.textManualInjection);
        setButton.setText("Manaual Injection");

    }

}
