package com.example.junpeng.insulinpump;

import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

public class InsulinFragment extends Fragment {
    public static InsulinFragment newInstance() {
        InsulinFragment fragment = new InsulinFragment();
        return fragment;
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        return inflater.inflate(R.layout.insulin_fragment, container, false);
    }
    @Override
    public void onViewCreated(View view, @Nullable Bundle savedInstanceState) {
        TextView textView = (TextView) getView().findViewById(R.id.textView7);
        textView.setText("Insulin Remain");

        TextView textView1 = (TextView) getView().findViewById(R.id.textViewInsulinRemain);
        textView1.setText("50%");

    }
}