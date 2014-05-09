package com.example.qiebluetoothchat;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.PrintStream;
import java.util.UUID;

import android.os.Bundle;
import android.app.Activity;
import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.bluetooth.BluetoothSocket;
import android.content.Intent;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.view.Menu;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends Activity implements SensorEventListener{
	private static final int REQUEST_ENABLE_BT = 1 ;
	public String address = "B4:74:9F:F1:50:F1";
	public UUID uuid = UUID.fromString("00001101-0000-1000-8000-00805F9B34FB") ;
	public Button send ;
	public CheckBox cb;
	public TextView status, client,server,sensorT;
	public EditText pesan ;
	public BluetoothAdapter btAdapter =null ;
	public BluetoothDevice btDevice =null ;
	public BluetoothSocket btSocket =null ;
	public PrintStream ps,ps1,ps2 ;
	public BufferedReader br , brl;
	public InputStreamReader isr,isrl;
	public String msg ,inmsg ;
	public Thread t1;
	public Sensor sensor;
	public SensorManager sm;
	public float x[] = {0,0,0};
	public float c,y,z ;
	public boolean run = false ;
	
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        cb = (CheckBox) findViewById(R.id.on);
        send = (Button) findViewById(R.id.send);
        server = (TextView) findViewById(R.id.server);
        client = (TextView) findViewById(R.id.client);
        status = (TextView) findViewById(R.id.status);
        pesan = (EditText) findViewById(R.id.pesan);
        sensorT = (TextView) findViewById(R.id.sensor);
    	btAdapter = BluetoothAdapter.getDefaultAdapter();
    	sm = (SensorManager) getSystemService(SENSOR_SERVICE);
    	sensor = sm.getDefaultSensor(Sensor.TYPE_ACCELEROMETER);
        sm.registerListener(this, sensor,SensorManager.SENSOR_DELAY_NORMAL);
        cb.setOnClickListener(new View.OnClickListener() {
			@Override
			public void onClick(View v) {
				if(cb.isChecked()){
					loadDriver();
					connet();
				}else if(cb.isChecked()==false){
					try {
						btSocket.close();
					} catch (IOException e) {}
					btAdapter.disable();
					finish();
				}
			}
		});
        
        send.setOnClickListener(new View.OnClickListener() {
			@Override
			public void onClick(View v) {
				t1.start();
			}
		});
        t1 = new Thread(new Runnable(){
			@Override
			public void run() {
				while(true){
					send(x);
					try {
						if(btSocket.getInputStream()!=null){
							read();
						}
					} catch (IOException e) {	}
				}
			}
        });
    }
    
    public void loadDriver(){
    	if(btAdapter==null){
    		status.setText(" failed ");
    	}else{
    		if(btAdapter.isEnabled()){
    			status.setText("Bluetooth on");
    		}else{
    			Intent enablebt = new Intent(btAdapter.ACTION_REQUEST_ENABLE);
    			startActivityForResult(enablebt,REQUEST_ENABLE_BT);
    		}
    	}
    	try {
			status.setText("loading");
			Thread.sleep(10000);
		} catch (InterruptedException e) {
			status.setText("error ");
		}
    }
    public void connet(){
    	btDevice = btAdapter.getRemoteDevice(address);
    	try {
			btSocket = btDevice.createRfcommSocketToServiceRecord(uuid);
			status.setText("pairing");
		} catch (IOException e) {
			status.setText("Rfcommsocket");
			}
    	btAdapter.cancelDiscovery();
    	status.setText("cancelDiscovery");
    	try {
			btSocket.connect();
			status.setText("connect");
		} catch (IOException e) {
			status.setText("not connect");
		}
    }
    public void read() {
    	try {
			 isrl = new InputStreamReader(btSocket.getInputStream());
			 brl = new BufferedReader(isrl);
			 inmsg = brl.readLine();
		} catch (IOException e) {	}
		//server.setText(inmsg);
    }
    public void send(float[] x){
    	int i = 0;
    	while(i<3){
    		try {
    			ps = new PrintStream(btSocket.getOutputStream());
    		} catch (IOException e) {
    		    status.setText("GetOutData failed");
    		}
    		float nilai1 = x[i];
    		String nilai3 = String.valueOf(nilai1);
    		ps.println(nilai3);
    		i++;
    	}
    }
    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        getMenuInflater().inflate(R.menu.main, menu);
        return true;
    }
	@Override
	public void onAccuracyChanged(Sensor sensor, int accuracy) {
	}

	@Override
	public void onSensorChanged(SensorEvent event) {
		this.x[0] = event.values[0];
		this.x[1] = event.values[1];
		this.x[2] = event.values[2];
		sensorT.setText("X: "+event.values[0]+"Y : "+event.values[1]+"Z : "+event.values[2]);
		
	}
}
