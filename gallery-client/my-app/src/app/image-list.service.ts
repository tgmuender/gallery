import { Injectable } from '@angular/core';
import { PreviewImage} from "./PreviewImage";
import { Observable} from "rxjs/Observable";
import { of } from "rxjs/observable/of";
import { HttpClient, HttpHeaders} from "@angular/common/http";

@Injectable()
export class ImageListService {

  private imagesUrl = 'http://localhost:8000/images.json';

  getImages(): Observable<PreviewImage[]> {
    return this.http.get<PreviewImage[]>(this.imagesUrl)
  }

  constructor(
    private http: HttpClient) { }

}
