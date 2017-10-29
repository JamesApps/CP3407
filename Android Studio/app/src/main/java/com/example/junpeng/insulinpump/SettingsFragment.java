package com.example.junpeng.insulinpump;

import android.media.AudioManager;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.SeekBar;
import android.widget.TextView;

public class SettingsFragment extends Fragment  {
    public static SettingsFragment newInstance() {
        SettingsFragment fragment = new SettingsFragment();
        return fragment;
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);

    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {


        return inflater.inflate(R.layout.settings_fragment, container, false);
    }

    @Override
    public void onViewCreated(View view, @Nullable Bundle savedInstanceState) {
        TextView textView = (TextView) getView().findViewById(R.id.textView);
        textView.setText("Settings");
        TextView textView1 = (TextView) getView().findViewById(R.id.textView1);
        textView1.setText("Brightness");
        TextView textView2 = (TextView) getView().findViewById(R.id.textView2);
        textView2.setText("Sound");
        TextView textView3 = (TextView) getView().findViewById(R.id.textView3);
        textView3.setText("Font Size");

        Button setButton = (Button) getView().findViewById(R.id.Set);
        setButton.setText("Set");
    }
}
