using UnityEngine;
using System.Collections;
using Photon.Pun;

namespace VRStudies { namespace SinglePlayer {

public class Cube : MonoBehaviourPunCallbacks {

        // Joinイベントをリッスン
	//------------------------------------------------------------------------------------------------------------------------------//
	public override void OnJoinedRoom() {

		// ルームログイン後に呼ぶ
		CreateCube ();
	}

	//------------------------------------------------------------------------------------------------------------------------------//
	void CreateCube () {
		// Photon経由で自分のアバターを動的に生成
		// 自分のアバターが他クライアント上にも自動で生成される = 他クライアントが生成したアバターは自クライアント上に自動で生成される
		GameObject cube = PhotonNetwork.Instantiate("Cube1",new Vector3(0,0,0), Quaternion.identity, 0);
		void Update(){
			if (!photonView.IsMine){
				cube.transform.parent = GameObject.Find("RightHandAnchor").transform;
			}
		//photonView.RPC(nameof(Track), RpcTarget.All);
		//GameObject cube = PhotonNetwork.Instantiate("Cube1", GameObject.Find("RightHandAnchor").transform.position, Quaternion.identity, 0);
        //cube.transform.parent = GameObject.Find("RightHandAnchor").transform;
		}
	//[PunRPC]
	//private void Track(){

		//}

	}
	
}
}}