package com.example.tom.picwk;

import android.content.Intent;
import android.os.Bundle;
import android.os.Parcelable;
import android.support.v7.app.AppCompatActivity;
import android.util.Pair;
import android.view.View;
import android.widget.EditText;
import android.widget.ProgressBar;
import android.widget.TextView;

import com.loopj.android.http.*;
import com.squareup.picasso.Picasso;
import com.squareup.picasso.RequestCreator;

import cz.msebera.android.httpclient.Header;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.net.URL;
import java.net.URLEncoder;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

    }

    public void sends(View w) throws IOException, JSONException {
        EditText  txtEdit = (EditText) findViewById(R.id.editText);
        final TextView  txtView = (TextView) findViewById(R.id.textView);
        final ProgressBar progressBar = (ProgressBar) findViewById(R.id.progressBar);

        AsyncHttpClient client = new AsyncHttpClient();
        client.setConnectTimeout(1000 * 60 * 5);
        client.setTimeout(1000 * 60 * 5);
        RequestParams params = new RequestParams();
        params.put("text", txtEdit.getText().toString());
        client.post("https://4a99a674.ngrok.io/execute", params, new TextHttpResponseHandler() {
                    @Override
                    public  void onStart() {
                        progressBar.setVisibility(ProgressBar.VISIBLE);
                    }
                    @Override
                    public void onSuccess(int statusCode, Header[] headers, String res) {
                        // called when response HTTP status is "200 OK"
                        System.out.println(res);
                        try {
                            JSONObject result = new JSONObject(res);

                            Intent intent = new Intent(MainActivity.this, AboutActivity.class);
                            intent.putExtra("url",  result.getJSONArray("url").toString());
                            intent.putExtra("tags", result.getJSONArray("tags").toString());
                            //  intent.putExtra("tags", (Parcelable) result.getJSONArray("tags"));
                            startActivity(intent);
                        } catch (JSONException e) {
                            e.printStackTrace();
                        }
                    }

                    @Override
                    public void onFailure(int statusCode, Header[] headers, String res, Throwable t) {
                        // called when response HTTP status is "4XX" (eg. 401, 403, 404)
                    }

                    public void onFinish() {
                        progressBar.setVisibility(ProgressBar.INVISIBLE);
                    }
                }
        );

    }

}

