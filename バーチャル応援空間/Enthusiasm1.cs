using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Enthusiasm1 : MonoBehaviour {

    GameObject hakusyu;
    claps script; //Scriptが入る変数
　　 Animation anime;

    // Use this for initialization
    void Start () {
        hakusyu = GameObject.Find ("Text (1)"); 
        script = hakusyu.GetComponent<claps>(); //Scriptを取得して変数に格納する
        anime = GameObject.Find("Audience 1").GetComponent<Animation>();
    }

    // Update is called once per frame
    void Update () {

        int moriagari = script.clap_count; //新しく変数を宣言してその中にscriptの変数を代入する
        if (moriagari>9)
        {
            anime.Play("celebration");
        }
        
    }
}