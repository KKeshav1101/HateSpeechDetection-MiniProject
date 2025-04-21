<h1>Hate Speech Detection - Mini Project</h1>
By Keshav K, Raahul Kumar and Shruti Rajesh
<h2>Comparative Study from all our implementations</h2>
<table>
  <tr>
    <th>Model</th>
    <th>F1-Score</th>
    <th>Accuracy</th>
    <th>Precision</th>
    <th>Recall</th>
    <th>Time/Step (ms)</th>
    <th>BIN File Size (MB)</th>
  </tr>
  <tr>
    <td>LSTM2x</td>
    <td>0.86</td>
    <td>0.86</td>
    <td>0.86</td>
    <td>0.86</td>
    <td>1000</td>
    <td>31.3</td>
  </tr>
  <tr>
    <td>BiGRU</td>
    <td>0.87</td>
    <td>0.87</td>
    <td>0.87</td>
    <td>0.87</td>
    <td>141</td>
    <td>100</td>
  </tr>
  <tr>
    <td>Random Forest</td>
    <td>0.85</td>
    <td>0.85</td>
    <td>0.85</td>
    <td>0.85</td>
    <td>~1000</td>
    <td>402</td>
  </tr>
  <tr>
    <td>Gradient Boost Classifier</td>
    <td>0.68</td>
    <td>0.70</td>
    <td>0.74</td>
    <td>0.70</td>
    <td>~1000</td>
    <td>0.287</td>
  </tr>
  <tr>
    <td>XGBoost</td>
    <td>0.79</td>
    <td>0.79</td>
    <td>0.79</td>
    <td>0.79</td>
    <td>~1000</td>
    <td>0.287</td>
  </tr>
  <tr>
    <td>Ensemble</td>
    <td>0.83</td>
    <td>0.84</td>
    <td>0.84</td>
    <td>0.84</td>
    <td>~8000</td>
    <td>804</td>
  </tr>
</table>
