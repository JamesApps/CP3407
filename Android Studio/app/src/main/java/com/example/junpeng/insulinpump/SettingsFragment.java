package com.example.junpeng.insulinpump;

import android.content.Context;
import android.content.SharedPreferences;
import android.media.AudioManager;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.util.TypedValue;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.SeekBar;
import android.widget.SeekBar.OnSeekBarChangeListener;
import android.widget.TextView;

import static android.content.Context.MODE_PRIVATE;

public class SettingsFragment extends Fragment  {

    private SeekBar soundSeekbar;
    private SeekBar fontSeekbar;
    private SeekBar brightnessSeekBar;
    private AudioManager audioManager;
    private SharedPreferences sharedPreferences;

    private EditText edittext;

    public static SettingsFragment newInstance() {
        SettingsFragment fragment = new SettingsFragment();
        return fragment;
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);


        getActivity().setVolumeControlStream(AudioManager.STREAM_MUSIC);
        soundControls();
        fontControls();
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

        SeekBar brightnessSeekBar = (SeekBar) getView().findViewById(R.id.BrightnessBar);
        SeekBar soundSeekBar = (SeekBar) getView().findViewById(R.id.SoundBar);
        SeekBar fontSeekBar = (SeekBar) getView().findViewById(R.id.FontBar);

    }
    private void soundControls()
    {
        try
        {
            SeekBar soundSeekbar = (SeekBar) getView().findViewById(R.id.SoundBar);
            audioManager = (AudioManager) getActivity().getSystemService(Context.AUDIO_SERVICE);
            soundSeekbar.setMax(audioManager.getStreamMaxVolume(AudioManager.STREAM_MUSIC));
            soundSeekbar.setProgress(audioManager.getStreamVolume(AudioManager.STREAM_MUSIC));


            soundSeekbar.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener()
            {
                @Override
                public void onStopTrackingTouch(SeekBar arg0)
                {
                }

                @Override
                public void onStartTrackingTouch(SeekBar arg0)
                {
                }

                @Override
                public void onProgressChanged(SeekBar arg0, int progress, boolean arg2)
                {
                    audioManager.setStreamVolume(AudioManager.STREAM_MUSIC,
                            progress, 0);
                }
            });
        }
        catch (Exception e)
        {
            e.printStackTrace();
        }
    }

    private void brightnessControls()
    {
        try
        {
            SeekBar brightnessSeekbar = (SeekBar) getView().findViewById(R.id.BrightnessBar);

            brightnessSeekbar.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener()
            {
                @Override
                public void onStopTrackingTouch(SeekBar arg0)
                {
                }

                @Override
                public void onStartTrackingTouch(SeekBar arg0)
                {
                }

                @Override
                public void onProgressChanged(SeekBar arg0, int progress, boolean arg2)
                {
                }
            });
        }
        catch (Exception e)
        {
            e.printStackTrace();
        }
    }

    private void fontControls()
    {
        try
        {
            sharedPreferences = getActivity().getPreferences(MODE_PRIVATE);
            SeekBar fontSeekbar = (SeekBar) getView().findViewById(R.id.FontBar);

            float fontSize = sharedPreferences.getFloat("fontsize", 12);
            fontSeekbar.setProgress((int)fontSize);
            edittext.setTextSize(TypedValue.COMPLEX_UNIT_PX,fontSeekbar.getProgress());

            fontSeekbar.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener()
            {
                @Override
                public void onStopTrackingTouch(SeekBar fontSeekBar)
                {
                    sharedPreferences = getActivity().getPreferences(MODE_PRIVATE);
                    SharedPreferences.Editor ed =  sharedPreferences.edit();
                }

                @Override
                public void onStartTrackingTouch(SeekBar fontSeekBar)
                {
                }

                @Override
                public void onProgressChanged(SeekBar fontSeekBar, int progress, boolean fromUser)
                {
                    edittext.setTextSize(TypedValue.COMPLEX_UNIT_PX,progress);
                }
            });
        }
        catch (Exception e)
        {
            e.printStackTrace();
        }
    }
};

