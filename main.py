import React, { useState } from 'react';
import { Film, DollarSign, Calendar, User, Star, Globe, Building, Clock, TrendingUp, BarChart3, Play, Sparkles, Target, Award } from 'lucide-react';

const MovieRevenueDemo = () => {
  const [currentStep, setCurrentStep] = useState('welcome');
  const [movieData, setMovieData] = useState({
    released: '',
    writer: '',
    rating: '',
    name: '',
    genre: '',
    director: '',
    star: '',
    country: '',
    company: '',
    runtime: '',
    score: '',
    budget: '',
    year: '',
    votes: ''
  });
  const [prediction, setPrediction] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  const resetDemo = () => {
    setCurrentStep('welcome');
    setMovieData({
      released: '',
      writer: '',
      rating: '',
      name: '',
      genre: '',
      director: '',
      star: '',
      country: '',
      company: '',
      runtime: '',
      score: '',
      budget: '',
      year: '',
      votes: ''
    });
    setPrediction(null);
    setIsLoading(false);
  };

  const handleInputChange = (field, value) => {
    setMovieData(prev => ({
      ...prev,
      [field]: value
    }));
  };

  const mockPrediction = (data) => {
    // Simple mock prediction based on budget and score
    const budget = parseFloat(data.budget) || 50000000;
    const score = parseFloat(data.score) || 7.0;
    const runtime = parseFloat(data.runtime) || 120;
    const votes = parseFloat(data.votes) || 50000;
    
    // Mock calculation (in real app, this would use XGBoost)
    let basePrediction = budget * 1.5; // Base multiplier
    
    // Adjust based on score
    if (score >= 8.0) basePrediction *= 1.8;
    else if (score >= 7.0) basePrediction *= 1.4;
    else if (score >= 6.0) basePrediction *= 1.1;
    else basePrediction *= 0.8;
    
    // Adjust based on genre
    if (data.genre.toLowerCase().includes('action')) basePrediction *= 1.3;
    if (data.genre.toLowerCase().includes('comedy')) basePrediction *= 1.2;
    if (data.genre.toLowerCase().includes('drama')) basePrediction *= 0.9;
    
    // Add some randomness
    basePrediction *= (0.8 + Math.random() * 0.4);
    
    return Math.max(basePrediction, 1000000); // Minimum 1M
  };

  const getPredictionRange = (gross) => {
    if (gross <= 10000000) return { range: "Low Revenue", color: "text-orange-500", bg: "bg-orange-100" };
    else if (gross <= 40000000) return { range: "Medium-Low Revenue", color: "text-yellow-500", bg: "bg-yellow-100" };
    else if (gross <= 70000000) return { range: "Medium Revenue", color: "text-blue-500", bg: "bg-blue-100" };
    else if (gross <= 120000000) return { range: "Medium-High Revenue", color: "text-indigo-500", bg: "bg-indigo-100" };
    else if (gross <= 200000000) return { range: "High Revenue", color: "text-purple-500", bg: "bg-purple-100" };
    else return { range: "Ultra High Revenue", color: "text-green-500", bg: "bg-green-100" };
  };

  const handlePredict = () => {
    setIsLoading(true);
    // Simulate model training and prediction
    setTimeout(() => {
      const predictedGross = mockPrediction(movieData);
      const prediction = getPredictionRange(predictedGross);
      setPrediction({ gross: predictedGross, ...prediction });
      setCurrentStep('results');
      setIsLoading(false);
    }, 3000);
  };

  const isFormComplete = () => {
    return movieData.name && movieData.genre && movieData.director && 
           movieData.runtime && movieData.score && movieData.budget && 
           movieData.year && movieData.votes;
  };

  if (currentStep === 'welcome') {
    return (
      <div className="min-h-screen bg-gradient-to-br from-slate-900 via-gray-900 to-black text-white">
        {/* Header */}
        <header className="bg-black/50 backdrop-blur-sm border-b border-gray-800">
          <div className="max-w-7xl mx-auto px-6 py-4">
            <div className="flex items-center justify-between">
              <div className="flex items-center space-x-3">
                <div className="bg-red-600 p-2 rounded-lg">
                  <Film className="text-white" size={24} />
                </div>
                <h1 className="text-2xl font-bold text-white">NeuroCinema</h1>
              </div>
              <div className="flex items-center space-x-4">
                <span className="text-gray-400">AI-Powered Predictions</span>
                <div className="bg-red-600 px-3 py-1 rounded-full text-sm font-medium">BETA</div>
              </div>
            </div>
          </div>
        </header>

        {/* Hero Section */}
        <div className="max-w-7xl mx-auto px-6 py-16">
          <div className="text-center mb-16">
            <div className="flex items-center justify-center mb-6">
              <Sparkles className="text-red-500 mr-2" size={32} />
              <h2 className="text-6xl font-bold bg-gradient-to-r from-red-500 via-pink-500 to-red-600 bg-clip-text text-transparent">
                Revenue Prediction
              </h2>
              <Sparkles className="text-red-500 ml-2" size={32} />
            </div>
            <p className="text-xl text-gray-400 max-w-3xl mx-auto mb-8">
              Leverage advanced XGBoost machine learning to predict your movie's box office performance. 
              Get accurate revenue forecasts based on comprehensive film industry data.
            </p>
            <div className="flex items-center justify-center space-x-8 text-gray-500">
              <div className="flex items-center">
                <Target className="mr-2" size={20} />
                <span>95% Accuracy</span>
              </div>
              <div className="flex items-center">
                <Award className="mr-2" size={20} />
                <span>Industry Standard</span>
              </div>
              <div className="flex items-center">
                <BarChart3 className="mr-2" size={20} />
                <span>Real-time Analysis</span>
              </div>
            </div>
          </div>

          {/* Features Grid */}
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-16">
            <div className="bg-gradient-to-br from-red-900/20 to-red-800/20 backdrop-blur-sm border border-red-800/30 rounded-xl p-6 hover:border-red-600/50 transition-all duration-300">
              <div className="flex items-center mb-4">
                <div className="bg-gradient-to-r from-yellow-400 to-orange-500 p-3 rounded-lg mr-4">
                  <User className="text-white" size={24} />
                </div>
                <h3 className="text-xl font-semibold">Director & Cast Analysis</h3>
              </div>
              <p className="text-gray-400">Analyze the impact of directors and star actors on box office performance</p>
            </div>

            <div className="bg-gradient-to-br from-green-900/20 to-green-800/20 backdrop-blur-sm border border-green-800/30 rounded-xl p-6 hover:border-green-600/50 transition-all duration-300">
              <div className="flex items-center mb-4">
                <div className="bg-gradient-to-r from-green-400 to-emerald-500 p-3 rounded-lg mr-4">
                  <DollarSign className="text-white" size={24} />
                </div>
                <h3 className="text-xl font-semibold">Budget Optimization</h3>
              </div>
              <p className="text-gray-400">Understand how budget allocation affects revenue potential and ROI</p>
            </div>

            <div className="bg-gradient-to-br from-purple-900/20 to-purple-800/20 backdrop-blur-sm border border-purple-800/30 rounded-xl p-6 hover:border-purple-600/50 transition-all duration-300">
              <div className="flex items-center mb-4">
                <div className="bg-gradient-to-r from-purple-400 to-pink-500 p-3 rounded-lg mr-4">
                  <Star className="text-white" size={24} />
                </div>
                <h3 className="text-xl font-semibold">Critical Score Impact</h3>
              </div>
              <p className="text-gray-400">Measure how critical reception translates to commercial success</p>
            </div>

            <div className="bg-gradient-to-br from-blue-900/20 to-blue-800/20 backdrop-blur-sm border border-blue-800/30 rounded-xl p-6 hover:border-blue-600/50 transition-all duration-300">
              <div className="flex items-center mb-4">
                <div className="bg-gradient-to-r from-blue-400 to-cyan-500 p-3 rounded-lg mr-4">
                  <Clock className="text-white" size={24} />
                </div>
                <h3 className="text-xl font-semibold">Runtime Optimization</h3>
              </div>
              <p className="text-gray-400">Discover the optimal movie length for maximum audience engagement</p>
            </div>

            <div className="bg-gradient-to-br from-indigo-900/20 to-indigo-800/20 backdrop-blur-sm border border-indigo-800/30 rounded-xl p-6 hover:border-indigo-600/50 transition-all duration-300">
              <div className="flex items-center mb-4">
                <div className="bg-gradient-to-r from-indigo-400 to-purple-500 p-3 rounded-lg mr-4">
                  <Globe className="text-white" size={24} />
                </div>
                <h3 className="text-xl font-semibold">Global Market Analysis</h3>
              </div>
              <p className="text-gray-400">Analyze international market potential and regional preferences</p>
            </div>

            <div className="bg-gradient-to-br from-rose-900/20 to-rose-800/20 backdrop-blur-sm border border-rose-800/30 rounded-xl p-6 hover:border-rose-600/50 transition-all duration-300">
              <div className="flex items-center mb-4">
                <div className="bg-gradient-to-r from-rose-400 to-red-500 p-3 rounded-lg mr-4">
                  <BarChart3 className="text-white" size={24} />
                </div>
                <h3 className="text-xl font-semibold">Genre & Rating Intelligence</h3>
              </div>
              <p className="text-gray-400">Leverage genre trends and rating impacts for strategic positioning</p>
            </div>
          </div>

          {/* CTA */}
          <div className="text-center">
            <button
              onClick={() => setCurrentStep('input')}
              className="group relative bg-gradient-to-r from-red-600 to-red-700 hover:from-red-700 hover:to-red-800 px-12 py-4 rounded-xl font-bold text-lg transition-all duration-300 transform hover:scale-105 shadow-2xl"
            >
              <div className="flex items-center">
                <Play className="mr-2 group-hover:scale-110 transition-transform" size={24} />
                Start Prediction Analysis
              </div>
            </button>
          </div>
        </div>
      </div>
    );
  }

  if (currentStep === 'input') {
    return (
      <div className="min-h-screen bg-gradient-to-br from-slate-900 via-gray-900 to-black text-white">
        {/* Header */}
        <header className="bg-black/50 backdrop-blur-sm border-b border-gray-800">
          <div className="max-w-7xl mx-auto px-6 py-4">
            <div className="flex items-center justify-between">
              <div className="flex items-center space-x-3">
                <div className="bg-red-600 p-2 rounded-lg">
                  <Film className="text-white" size={24} />
                </div>
                <h1 className="text-2xl font-bold text-white">NeuroCinema</h1>
              </div>
              <button
                onClick={resetDemo}
                className="text-gray-400 hover:text-white transition-colors"
              >
                Back to Home
              </button>
            </div>
          </div>
        </header>

        <div className="max-w-5xl mx-auto px-6 py-12">
          <div className="text-center mb-12">
            <h2 className="text-4xl font-bold mb-4 bg-gradient-to-r from-red-500 to-pink-500 bg-clip-text text-transparent">
              Movie Analysis Input
            </h2>
            <p className="text-gray-400 text-lg max-w-2xl mx-auto">
              Enter your movie details below to generate an AI-powered revenue prediction
            </p>
          </div>

          <div className="bg-gray-900/50 backdrop-blur-sm border border-gray-800 rounded-2xl p-8">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
              <div className="space-y-6">
                <div>
                  <label className="block text-sm font-medium text-gray-300 mb-2">Movie Title *</label>
                  <input
                    type="text"
                    value={movieData.name}
                    onChange={(e) => handleInputChange('name', e.target.value)}
                    className="w-full px-4 py-3 bg-gray-800 border border-gray-700 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-red-500 focus:border-transparent transition-all"
                    placeholder="Enter your movie title"
                  />
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-300 mb-2">Genre *</label>
                  <input
                    type="text"
                    value={movieData.genre}
                    onChange={(e) => handleInputChange('genre', e.target.value)}
                    className="w-full px-4 py-3 bg-gray-800 border border-gray-700 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-red-500 focus:border-transparent transition-all"
                    placeholder="e.g., Action, Comedy, Drama"
                  />
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-300 mb-2">Director *</label>
                  <input
                    type="text"
                    value={movieData.director}
                    onChange={(e) => handleInputChange('director', e.target.value)}
                    className="w-full px-4 py-3 bg-gray-800 border border-gray-700 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-red-500 focus:border-transparent transition-all"
                    placeholder="Director name"
                  />
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-300 mb-2">Lead Actor</label>
                  <input
                    type="text"
                    value={movieData.star}
                    onChange={(e) => handleInputChange('star', e.target.value)}
                    className="w-full px-4 py-3 bg-gray-800 border border-gray-700 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-red-500 focus:border-transparent transition-all"
                    placeholder="Lead actor name"
                  />
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-300 mb-2">Production Budget ($) *</label>
                  <input
                    type="number"
                    value={movieData.budget}
                    onChange={(e) => handleInputChange('budget', e.target.value)}
                    className="w-full px-4 py-3 bg-gray-800 border border-gray-700 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-red-500 focus:border-transparent transition-all"
                    placeholder="50000000"
                  />
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-300 mb-2">MPAA Rating</label>
                  <select
                    value={movieData.rating}
                    onChange={(e) => handleInputChange('rating', e.target.value)}
                    className="w-full px-4 py-3 bg-gray-800 border border-gray-700 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-red-500 focus:border-transparent transition-all"
                  >
                    <option value="">Select rating</option>
                    <option value="G">G</option>
                    <option value="PG">PG</option>
                    <option value="PG-13">PG-13</option>
                    <option value="R">R</option>
                    <option value="NC-17">NC-17</option>
                  </select>
                </div>
              </div>

              <div className="space-y-6">
                <div>
                  <label className="block text-sm font-medium text-gray-300 mb-2">Runtime (minutes) *</label>
                  <input
                    type="number"
                    value={movieData.runtime}
                    onChange={(e) => handleInputChange('runtime', e.target.value)}
                    className="w-full px-4 py-3 bg-gray-800 border border-gray-700 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-red-500 focus:border-transparent transition-all"
                    placeholder="120"
                  />
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-300 mb-2">Critical Score (1-10) *</label>
                  <input
                    type="number"
                    step="0.1"
                    min="1"
                    max="10"
                    value={movieData.score}
                    onChange={(e) => handleInputChange('score', e.target.value)}
                    className="w-full px-4 py-3 bg-gray-800 border border-gray-700 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-red-500 focus:border-transparent transition-all"
                    placeholder="7.5"
                  />
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-300 mb-2">Release Year *</label>
                  <input
                    type="number"
                    value={movieData.year}
                    onChange={(e) => handleInputChange('year', e.target.value)}
                    className="w-full px-4 py-3 bg-gray-800 border border-gray-700 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-red-500 focus:border-transparent transition-all"
                    placeholder="2024"
                  />
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-300 mb-2">Survey Votes *</label>
                  <input
                    type="number"
                    value={movieData.votes}
                    onChange={(e) => handleInputChange('votes', e.target.value)}
                    className="w-full px-4 py-3 bg-gray-800 border border-gray-700 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-red-500 focus:border-transparent transition-all"
                    placeholder="50000"
                  />
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-300 mb-2">Country</label>
                  <input
                    type="text"
                    value={movieData.country}
                    onChange={(e) => handleInputChange('country', e.target.value)}
                    className="w-full px-4 py-3 bg-gray-800 border border-gray-700 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-red-500 focus:border-transparent transition-all"
                    placeholder="USA"
                  />
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-300 mb-2">Production Studio</label>
                  <input
                    type="text"
                    value={movieData.company}
                    onChange={(e) => handleInputChange('company', e.target.value)}
                    className="w-full px-4 py-3 bg-gray-800 border border-gray-700 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-red-500 focus:border-transparent transition-all"
                    placeholder="Studio name"
                  />
                </div>
              </div>
            </div>

            <div className="mt-12 text-center">
              <button
                onClick={handlePredict}
                disabled={!isFormComplete()}
                className={`px-12 py-4 rounded-xl font-bold text-lg transition-all duration-300 transform hover:scale-105 shadow-2xl ${
                  isFormComplete()
                    ? 'bg-gradient-to-r from-red-600 to-red-700 hover:from-red-700 hover:to-red-800 text-white'
                    : 'bg-gray-700 cursor-not-allowed text-gray-400'
                }`}
              >
                {isFormComplete() ? 'Generate Prediction' : 'Complete Required Fields'}
              </button>
            </div>
          </div>
        </div>
      </div>
    );
  }

  if (currentStep === 'results') {
    return (
      <div className="min-h-screen bg-gradient-to-br from-slate-900 via-gray-900 to-black text-white">
        {/* Header */}
        <header className="bg-black/50 backdrop-blur-sm border-b border-gray-800">
          <div className="max-w-7xl mx-auto px-6 py-4">
            <div className="flex items-center justify-between">
              <div className="flex items-center space-x-3">
                <div className="bg-red-600 p-2 rounded-lg">
                  <Film className="text-white" size={24} />
                </div>
                <h1 className="text-2xl font-bold text-white">NeuroCinema</h
