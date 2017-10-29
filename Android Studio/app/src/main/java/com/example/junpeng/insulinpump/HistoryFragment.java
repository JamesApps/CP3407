package com.example.junpeng.insulinpump;

import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.TextView;

public class HistoryFragment extends Fragment {
    public static HistoryFragment newInstance() {
        HistoryFragment fragment = new HistoryFragment();
        return fragment;
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        return inflater.inflate(R.layout.history_fragment, container, false);
    }
    @Override
    public void onViewCreated(View view, @Nullable Bundle savedInstanceState) {
        TextView textView = (TextView) getView().findViewById(R.id.textView);
        textView.setText("History");
        Button setButton = (Button) getView().findViewById(R.id.ShowGraph);
        setButton.setText("Set");

    }
}