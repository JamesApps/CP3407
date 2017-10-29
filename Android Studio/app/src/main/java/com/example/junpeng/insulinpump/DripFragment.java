package com.example.junpeng.insulinpump;

import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.TextView;

public class DripFragment extends Fragment {
    public static DripFragment newInstance() {
        DripFragment fragment = new DripFragment();
        return fragment;
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        return inflater.inflate(R.layout.drip_fragment, container, false);
    }

    @Override
    public void onViewCreated(View view, @Nullable Bundle savedInstanceState) {
        TextView textView = (TextView) getView().findViewById(R.id.textView);
        textView.setText("Drip");
        TextView textView1 = (TextView) getView().findViewById(R.id.textView5);
        textView1.setText("Drip Quantity Per Day");
        TextView textView2 = (TextView) getView().findViewById(R.id.textView3);
        textView2.setText("Drip Frequency Per day");
        TextView textView3 = (TextView) getView().findViewById(R.id.textView10);
        textView3.setText("100u");
        TextView textView4 = (TextView) getView().findViewById(R.id.textView9);
        textView4.setText("24");

        Button setButton = (Button) getView().findViewById(R.id.DripSet);
        setButton.setText("Set");

    }
}
