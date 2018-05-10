import {Injectable} from "@angular/core";
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs/Observable";
import {ImageDetails} from "./ImageDetails";

@Injectable()
export class ImageDetailService {

  getImageDetails(imageName: string): Observable<ImageDetails> {
    return this.http.get<ImageDetails>('http://localhost:8000/metadata/' + imageName + '.json');
  }

  constructor(
    private http: HttpClient
  ){}

}
