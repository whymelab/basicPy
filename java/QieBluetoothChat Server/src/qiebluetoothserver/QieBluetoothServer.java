package qiebluetoothserver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintStream;
import java.util.Scanner;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.bluetooth.BluetoothStateException;
import javax.bluetooth.LocalDevice;
import javax.bluetooth.RemoteDevice;
import javax.bluetooth.UUID;
import javax.microedition.io.Connector;
import javax.microedition.io.StreamConnection;
import javax.microedition.io.StreamConnectionNotifier;

public class QieBluetoothServer {
    protected BufferedReader bf, bf2;
    protected PrintStream ps,ps2;
    protected InputStreamReader isr ,isr2;
    protected StreamConnectionNotifier streamConnNotifier ;
    protected UUID uuid ;
    protected StreamConnection connection;
    protected String connectionString;
    protected RemoteDevice dev;
    protected String x ,y, z ;
    protected static LocalDevice localDevice ;
    protected boolean run = true;
    protected static Thread thread1,thread2 ;
    public void Connect(){
        uuid = new UUID("0000110100001000800000805f9b2131",false);
        connectionString = "btspp://localhost:" + uuid +";name=Qie Bluetooth Server";
        try {
            streamConnNotifier = (StreamConnectionNotifier)Connector.open( connectionString );
        } catch (IOException ex) { 
            System.out.println("Error StreamConnNotifier");
        }
        System.out.println("Membuat saluran socket bluetooth ");
        try {
            connection = streamConnNotifier.acceptAndOpen();
        } catch (IOException ex) {  
            System.out.println("Error StreamConnection ");
        }
        System.out.println("Menyetujui dan membuka socket  ");
        try {
            dev = RemoteDevice.getRemoteDevice(connection);
        } catch (IOException ex) { 
            System.out.println("Error RemoteDevice ");
        }
        System.out.println("Mendapatkan data client ");
        System.out.println("Remote device address: "+dev.getBluetoothAddress());
        try {
            System.out.println("Remote device name: "+dev.getFriendlyName(true));
        } catch (IOException ex) { 
            System.out.println("Error Remotedeice name ");
        }
        while(run == true){
            try {
                isr = new InputStreamReader(connection.openDataInputStream());
            } catch (IOException ex) { }
            bf = new BufferedReader(isr);
            try {
                x = bf.readLine();
            } catch (IOException ex) { }
            System.out.println("Pesan dari Android : "+x);
            if(isr !=null){
                try {
                    ps = new PrintStream(connection.openOutputStream());
                } catch (IOException ex) { }
                isr2 = new InputStreamReader(System.in);
                bf2 = new BufferedReader(isr2);
                try {
                    System.out.print("Pesan dari Komputer : ");
                    y = bf2.readLine();
                } catch (IOException ex) { }
                ps.println(y);
            }
        }
    }
    public static void main(String[] args) {
        /*thread1 = new Thread(new Runnable(){
                @Override
                public void run() {
                     Scanner scan = new Scanner(System.in);
                     System.out.print("Press any key to exit ");
                     String nilai = scan.nextLine();
                     if(nilai.equals("EXIT") ){
                         thread2.stop();
                         thread1.stop();
                     }
                }
        });*/
        thread2 = new Thread(new Runnable(){
            @Override
            public void run() {
                try {
                    Thread.sleep(2000);
                } catch (InterruptedException ex) {}
                try {
                    localDevice = LocalDevice.getLocalDevice();
                } catch (BluetoothStateException ex) {  }
                System.out.println("================================================");
                System.out.println("Address     : "+localDevice.getBluetoothAddress());
                System.out.println("Name        : "+localDevice.getFriendlyName());
                System.out.println("================================================");
                System.out.println("Loading . . .");
                QieBluetoothServer Server = new QieBluetoothServer();
                Server.Connect();
            }
        });
        //thread1.start();
        thread2.start();
        try {
            //thread1.join();
            thread2.join();
        } catch (InterruptedException ex) {  }
        System.exit(0);
    }
}
