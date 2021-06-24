using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class claps : MonoBehaviour
{
    public float x;
    public Microphone_input _Microphone_input;
    public Microphone_input _MyMicrophone_input;
    //
    public int fps_count=0;
    public int clap_count=0;
    //publicはglobalみたいなもの。他のclassやコンポーネント上からもいじれるようになる。

	// Use this for initialization
	void Start ()
    {
        _MyMicrophone_input = _Microphone_input.GetComponent<Microphone_input>();  
	}
	
	// Update is called once per frame
	void Update ()
    {
        //this.GetComponent<Text>().text = clap_count.ToString();
        //.textでTextに値を代入する。ToString()で数字から文字列に変換
        x = _MyMicrophone_input.DifLoudness;
        
        if (x >= 1.5)
        {
            fps_count++;
        }
        else
        {
            if(1<=fps_count&&fps_count<=5)
            {
                clap_count++;

            }
            fps_count = 0;
        }
	}
}
