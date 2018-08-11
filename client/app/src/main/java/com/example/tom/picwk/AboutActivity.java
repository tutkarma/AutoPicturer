package com.example.tom.picwk;

import android.content.Intent;
import android.graphics.drawable.Drawable;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.Gravity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.animation.Animation;
import android.widget.AdapterView;
import android.widget.Gallery;
import android.widget.HorizontalScrollView;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.ProgressBar;
import android.widget.TextView;

import com.squareup.picasso.MemoryPolicy;
import com.squareup.picasso.Picasso;
import com.squareup.picasso.RequestCreator;

import org.json.JSONArray;
import org.json.JSONException;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;


public class AboutActivity extends AppCompatActivity {

    private LinearLayout mGallery;
    private LayoutInflater mInflater;
    private HorizontalScrollView horizontalScrollView;
    ImageView selectedImage;

    public int idx_image = 0;
    public JSONArray image_list;
    public List<RequestCreator> load_list = new ArrayList<>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_about);
        ProgressBar progressBar = (ProgressBar) findViewById(R.id.progressBar);
        progressBar.setVisibility(ProgressBar.VISIBLE);
        String url = getIntent().getExtras().getString("url");

        try {
            JSONArray tags_list = new JSONArray(getIntent().getExtras().getString("tags"));
            String tags = "";
            for (int i = 0; i < tags_list.length(); i++) {
                tags += tags_list.getString(i) + " ";
            }
            TextView  txtView = (TextView) findViewById(R.id.textView4);
            txtView.setText(tags);
            image_list = new JSONArray(url);
            for (int i = 0; i < image_list.length(); i++) {
                load_list.add(Picasso.get().load(image_list.getString(i)));
            }



            LinearLayout layout = (LinearLayout) findViewById(R.id.linear);
            for (int i = 0; i < load_list.size(); i++) {
                ImageView imageView = new ImageView(this);
                imageView.setId(i);
                LinearLayout.LayoutParams layoutParams = new LinearLayout.LayoutParams(LinearLayout.LayoutParams.WRAP_CONTENT, LinearLayout.LayoutParams.WRAP_CONTENT);
                layoutParams.gravity = Gravity.TOP | Gravity.END;
                imageView.setLayoutParams(layoutParams);

                imageView.setPadding(2, 2, 2, 2);
                load_list.get(i).resize(1100, 600).centerInside().into(imageView);
                layout.addView(imageView);
            }


        } catch (JSONException e) {
            e.printStackTrace();
            Intent intent = new Intent(AboutActivity.this, MainActivity.class);
            startActivity(intent);
        }
        progressBar.setVisibility(ProgressBar.INVISIBLE);
    }

    public void back(View w) {
        Intent intent = new Intent(AboutActivity.this, MainActivity.class);
        startActivity(intent);
    }


}
