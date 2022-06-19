using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Photon.Pun;

public class ChangeSkybox : MonoBehaviour {

    public Material[] sky;
    int num = 0;

    void OnCollisionExit(Collision collision)
    {
        if (collision.gameObject.tag == "Center"){
            num += 1;
        if(num >= sky.Length)
        {
            num = 0;
        }
            GetComponent<PhotonView>().RPC("RPCChange", RpcTarget.All);
        }
    }
    [PunRPC]
    void RPCChange(){
        RenderSettings.skybox = sky[num];
    }
}