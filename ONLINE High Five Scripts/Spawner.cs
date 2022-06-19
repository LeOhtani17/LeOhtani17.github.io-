using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Photon.Pun;

public class Spawner : MonoBehaviour
{
    public List<ParticleSystem> effect;
    public SePlay seplay;
    public float count=0; 
    int c = 100;
    public void Spawn(int index)
    {
        if (count==1){
        }else{
            c=index;
            GetComponent<PhotonView>().RPC("SpawnRPC", RpcTarget.All);
        }
    }

    public void EffectStop(int index){
        c=index;
        GetComponent<PhotonView>().RPC("StopRPC", RpcTarget.All);
    }
    
    IEnumerator SoundStart(){
        seplay = GameObject.Find("SePlayer").GetComponent<SePlay>();
        while (count==1){
            seplay.PlaySound("SE"+c);
            yield return new WaitForSeconds(0.1f);
        }
    }
    
    [PunRPC]
    void SpawnRPC(){
        effect[c].Play();
        count=1;
        StartCoroutine("SoundStart");
    }
    [PunRPC]
    void StopRPC(){
        effect[c].Stop();
        if(count==1){
            count=0;
            StopCoroutine("SoundStart");
        }else{
            count=0;
        }
    }

    }

