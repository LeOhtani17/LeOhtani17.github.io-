using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ChangeVideo : MonoBehaviour
{
    public int vchange = 0;
    void OnCollisionExit(Collision collision)
    {
        if (collision.gameObject.tag == "Head"){
            vchange += 1;
        }
    }
}
